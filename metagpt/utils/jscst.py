import re


def merge_jsdoc(code: str, documented_code: str) -> str:
    """
    Merges JSDoc comments from the documented code into the original code.

    Args:
        code: The original JavaScript/TypeScript code.
        documented_code: The JavaScript/TypeScript code with JSDoc comments.

    Returns:
        The original code with JSDoc comments merged in.
    """

    # Pattern to match JSDoc comments and the code blocks they document
    jsdoc_pattern = re.compile(
        r"(/\*\*[\s\S]*?\*/)\s*(function|class|const|let|var|async|[a-zA-Z$_][a-zA-Z0-9$_]*\s*=\s*|export\s+(?:default\s+)?(?:function|class))"
    )

    # Collect JSDoc comments and corresponding documented code blocks
    documented_segments = jsdoc_pattern.findall(documented_code)

    # Dictionary to store code signatures as keys and their JSDoc as values
    jsdoc_map = {}
    for jsdoc_comment, code_signature_prefix in documented_segments:
        # Extract the full code signature
        code_signature_match = re.search(
            r"(function\s+[a-zA-Z$_][a-zA-Z0-9$_]*|class\s+[a-zA-Z$_][a-zA-Z0-9$_]*|const\s+[a-zA-Z$_][a-zA-Z0-9$_]*\s*=\s*|let\s+[a-zA-Z$_][a-zA-Z0-9$_]*\s*=\s*|var\s+[a-zA-Z$_][a-zA-Z0-9$_]*\s*=\s*)",
            documented_code[documented_code.find(jsdoc_comment):]
        )
        code_signature = code_signature_match.group(0) if code_signature_match else None
        if code_signature:
            jsdoc_map[code_signature.strip()] = jsdoc_comment

    # Merging JSDoc comments into the original code
    def insert_jsdoc(match):
        code_signature = match.group(0).strip()
        # Ensure proper insertion of JSDoc comment before the function signature
        for signature, jsdoc in jsdoc_map.items():
            if code_signature.startswith(signature):
                return f"{jsdoc}\n{code_signature}"
        return code_signature

    # Insert JSDoc comments into the original code based on their code signatures
    modified_code = re.sub(
        r"(function\s+[a-zA-Z$_][a-zA-Z0-9$_]*|class\s+[a-zA-Z$_][a-zA-Z0-9$_]*|const\s+[a-zA-Z$_][a-zA-Z0-9$_]*\s*=\s*|let\s+[a-zA-Z$_][a-zA-Z0-9$_]*\s*=\s*|var\s+[a-zA-Z$_][a-zA-Z0-9$_]*\s*=\s*)",
        insert_jsdoc,
        code
    )

    return modified_code
