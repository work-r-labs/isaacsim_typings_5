from __future__ import annotations
__all__ = ['ITokens', 'RESOLVE_FLAG_LEAVE_TOKEN_IF_NOT_FOUND', 'RESOLVE_FLAG_NONE', 'acquire_tokens_interface']
class ITokens:
    """
    
    The Carbonite Tokens Interface
    
    Interface for storing tokens and resolving strings containing them. Tokens are string pairs {name, value} that can be
    referenced in a string as `"some text ${token_name} some other text"`, where the token name starts with a sequence
    `"${"` and end with a first closing `"}"`.
    
    If a token with the name \\<token_name\\> has a defined value, then it will be substituted with its value.
    If the token does not have a defined value, an empty string will be used for the replacement. This interface will use
    the ISetting interface, if available, as storage and in such case tokens will be stored under the '/app/tokens' node.
    
    Note: The "$" symbol is considered to be special by the tokenizer and should be escaped by doubling it ("$" -> "$$")
    in order to be processed as just a symbol "$"
    Ex: "some text with $ sign" -> "some text with $$ sign"
    
    Single unescaped "$" signs are considered to be a bad practice to be used for token resolution but they are
    acceptable and will be resolved into single "$" signs and no warning will be given about it.
    
    Ex:
      "$" -> "$",
      "$$" -> "$",
      "$$$" -> "$$"
    
    It's better to use the helper function "escapeString" from the "TokensUtils.h" to produce a string
    that doesn't have any parts that could participate in tokenization. As a token name start with "${" and ends with the
    first encountered "}" it can contain "$" (same rules about escaping it apply) and "{" characters, however such cases
    will result in a warning being output to the log.
    Ex: for the string "${bar$${}" the token resolution process will consider the token name to be "bar${"
    (note that "$$" is reduced into a single "$") and a warning will be outputted into the log.
    
    Tokens are resolved recursively unless an error occurs. For instance:
    
    .. code-block:: python
        
        tokens.set_value("a", "${b}");
        tokens.set_value("b", "${c}");
        tokens.set_value("c", "hello ${d}");
        tokens.set_value("d", "world");
    
        tokens.resolve("${a}"); # will return "hello world"
    
    Environment variables are automatically available as tokens, if defined. These are specified with the text
    `${env:<var name>}` where `<var name>` is the name of the environment variable. The `env:` prefix is a reserved name,
    so any call to set_value() or set_initial_value() with a name that starts with `env:` will
    be rejected. The environment variable is read when needed and not cached in any way. An undefined environment
    variable behaves as an undefined token.
    
    Thread Safety: the interface's functions are not thread safe. It is responsibility of the user to use all necessary
    synchronization mechanisms if needed. All data passed into a plugin's function must be valid for the duration of the
    function call.
    """
    def exists(self, name: str) -> bool:
        """
        Checks for the existence of a token.
        
        Parameters:
            name: Token name not enclosed in "${" and "}".
        
        Returns:
            boolean: True if the token with the specified name exists; False if the token name does not exist or an error occurred.
        """
    def remove_token(self, name: str) -> bool:
        """
        Delete a token.
        
        Parameters:
            name: Token name not enclosed in "${" and "}".
        
        Returns:
            boolean: True if the operation was successful or the token did not exist. False if an error occurred.
        """
    def resolve(self, str: str, flags: int = 0) -> str:
        """
        Tries to resolve all tokens in the string buffer and returns the result.
        
        Parameters:
            str: The string to resolve.
            flags: (optional, defaults to RESOLVE_FLAG_NONE) Flags that modify the token resolution process.
        
        Returns:
            string: The resolved string, or None if an error occurs.
        """
    def set_initial_value(self, name: str, value: str) -> None:
        """
        Creates a token with the given name and value if it was non-existent. Otherwise does nothing.
        
        Parameters:
            name: Token name not enclosed in "${" and "}".
            value: Value to assign if the token does not previously exist.
        """
    def set_value(self, name: str, value: str) -> bool:
        """
        Sets a new value for the specified token, if the token didn't exist it will be created.
        
        Note: if the value is null then the token will be removed (see also: `remove_token` function). In this case true
        is returned if the token was successfully deleted or didn't exist.
        
        Parameters:
            name: Token name not enclosed in "${" and "}".
            value: New value for the token.
        
        Returns:
            boolean: True if the operation was successful, False if an error occurred.
        """
def acquire_tokens_interface(plugin_name: str = None, library_path: str = None) -> ITokens:
    ...
RESOLVE_FLAG_LEAVE_TOKEN_IF_NOT_FOUND: int = 1
RESOLVE_FLAG_NONE: int = 0
