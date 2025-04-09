from __future__ import annotations
__all__ = ['dump_graph_topology']
def dump_graph_topology(file_name: str, deterministic_and_simplified: bool = False) -> None:
    """
            Write the default execution controller's corresponding execution graph topology out as a GraphViz file.
            All subgraphs, nodes, and connections are written out in a sorted fashion according to their names.
    
            Args:
                file_name (str):                     The name of the file.
                deterministic_and_simplified (bool): Optional flag to create a simplified graph dump that is also
                                                     guaranteed to remain exactly the same each time it is generated.
                                                     This is done by omitting node topology indices and name hashes
                                                     from all labels, and using the same color for the entire graph.
                                                     This setting is mostly used for creating graph dumps that are
                                                     later used in automated unit tests.
    """
