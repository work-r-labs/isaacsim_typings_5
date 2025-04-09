import importlib
from pathlib import Path

from pybind11_stubgen import (
    CLIArgs,
    Printer,
    QualifiedName,
    Writer,
    stub_parser_from_args,
)

"""
Generate stubs for the isaacsim and pxr libraries.

We can't use the pybind11-stubgen cli tool directly because the whole isaacsim api
is not available at import time. It needs to go through a bootstrap process and start
a whole simulation app before everything is available to import. This script automates
that process for us.
"""

output_dir = Path(__file__).parent / "typings"


def make_stubs(module_name: str) -> None:
    """
    Generate stubs for the specified module using pybind11-stubgen with default settings.

    Args:
        module_name: Name of the module to generate stubs for
    """
    # Create a parser with default settings
    parser = stub_parser_from_args(
        CLIArgs(
            output_dir=str(output_dir),
            root_suffix=None,
            ignore_invalid_expressions=None,
            ignore_invalid_identifiers=None,
            ignore_unresolved_names=None,
            ignore_all_errors=False,
            enum_class_locations=[],
            numpy_array_wrap_with_annotated=False,
            numpy_array_use_type_var=False,
            numpy_array_remove_parameters=False,
            print_invalid_expressions_as_is=False,
            print_safe_value_reprs=None,
            exit_code=False,
            dry_run=False,
            stub_extension="pyi",
            module_name=module_name,
        )
    )

    # Create a printer with default settings
    printer = Printer(invalid_expr_as_ellipses=True)

    # Set up output directory
    out_dir = output_dir
    module_path = module_name.split(".")
    out_dir = out_dir.joinpath(*module_path[:-1])

    # Create writer with default pyi extension
    writer = Writer(stub_ext="pyi")

    # Import the module
    imported_module = importlib.import_module(module_name)

    # Parse and generate stubs
    module = parser.handle_module(QualifiedName.from_str(module_name), imported_module)
    parser.finalize()

    if module is None:
        raise RuntimeError(f"Can't parse {module_name}")

    # Create output directory and write stubs
    out_dir.mkdir(exist_ok=True, parents=True)
    writer.write_module(module, printer, to=out_dir, sub_dir=None)

    print(f"Stubs for {module_name} generated in {out_dir}")


def main():
    from isaacsim import SimulationApp

    simulation_app = SimulationApp({"headless": True})

    # now that the SimulationApp has started, these modules are available
    make_stubs("omni.isaac")
    make_stubs("omni.kit")
    make_stubs("carb")
    make_stubs("omni.usd")
    make_stubs("isaacsim")
    make_stubs("simulation_app")
    make_stubs("usdrt")
    make_stubs("warp")
    make_stubs("pxr")

    simulation_app.close()


if __name__ == "__main__":
    main()
