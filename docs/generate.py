import os

from openstix import definitions, objects, toolkit


def generate_rst(submodule, module_name, path):
    rst_filename = os.path.join(path, f"{submodule}.rst")
    header = f"{submodule}\n{'='*len(submodule)}\n\n"
    automodule_directive = (
        f".. automodule:: {module_name}.{submodule}\n    :members:\n    :undoc-members:\n    :show-inheritance:"
    )
    autosummary_directive = "\n\n.. autosummary:: \n    :toctree: _autosummary\n    :nosignatures:\n"

    with open(rst_filename, "w") as file:
        file.write(header + automodule_directive + autosummary_directive)

    return rst_filename


def generate_rst_for_module(module, output_dir):
    if not hasattr(module, "__all__"):
        return []

    module_name = module.__name__.replace("openstix.", "")

    path_list = [output_dir] + module_name.split(".")
    path = os.path.join(*path_list)
    os.makedirs(path, exist_ok=True)

    generated_files = []
    for submodule in module.__all__:
        rst_filename = generate_rst(submodule, module.__name__, path)
        generated_files.append(rst_filename)

    return generated_files


def generate_modules_rst(generated_files, output_dir):
    modules_rst_filename = os.path.join(output_dir, "modules.rst")
    toctree_entries = "\n   ".join(
        f"{os.path.relpath(file, output_dir).replace(os.sep, '/')}" for file in generated_files
    )

    with open(modules_rst_filename, "w") as file:
        file.write(f"Modules\n=======\n\n" f".. toctree::\n   :maxdepth: 2\n\n   {toctree_entries}\n")


def main():
    output_dir = "_generated"
    os.makedirs(output_dir, exist_ok=True)

    generated_files = []
    for module in [definitions, objects, toolkit]:
        generated_files.extend(generate_rst_for_module(module, output_dir))

    generate_modules_rst(generated_files, output_dir)


if __name__ == "__main__":
    main()
