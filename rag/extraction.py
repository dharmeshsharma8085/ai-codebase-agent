import ast


def extract_code_structure(file_path: str):
    """Extract Python code structure and source ranges."""

    with open(file_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    tree = ast.parse(source_code)
    source_lines = source_code.splitlines()

    imports = []
    classes = []
    functions = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):
            for name in node.names:
                imports.append({
                    "name": name.name,
                    "line": node.lineno,
                })

        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""

            for name in node.names:
                imports.append({
                    "name": f"{module}.{name.name}",
                    "line": node.lineno,
                })

        elif isinstance(node, ast.ClassDef):
            classes.append({
                "name": node.name,
                "start_line": node.lineno,
                "end_line": node.end_lineno,
                "code": "\n".join(
                    source_lines[
                        node.lineno - 1 : node.end_lineno
                    ]
                ),
            })

        elif isinstance(
            node,
            (ast.FunctionDef, ast.AsyncFunctionDef),
        ):
            functions.append({
                "name": node.name,
                "start_line": node.lineno,
                "end_line": node.end_lineno,
                "code": "\n".join(
                    source_lines[
                        node.lineno - 1 : node.end_lineno
                    ]
                ),
            })

    return {
        "file": file_path,
        "imports": imports,
        "classes": classes,
        "functions": functions,
    }