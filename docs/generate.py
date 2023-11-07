import os
from openstix import definitions, objects, extensions

HEADER_TEMPLATE = "{}\n{}\n\n"

AUTOMODULE_TEMPLATE = """
.. automodule:: {module_name}.{submodule}
    :members:
    :undoc-members:
    :show-inheritance:
"""

TOCTREE_TEMPLATE = """
.. toctree::
   :maxdepth: 2
   :caption: {caption}

   {entries}
"""

class RSTGenerator:
    def __init__(self, output_dir="_generated"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
    
    @staticmethod
    def write_to_file(filename, content):
        with open(filename, "w") as file:
            file.write(content)

    @staticmethod
    def create_header(submodule):
        return HEADER_TEMPLATE.format(submodule, '=' * len(submodule))

    @staticmethod
    def create_automodule_directive(module_name, submodule):
        return AUTOMODULE_TEMPLATE.format(module_name=module_name, submodule=submodule)

    def generate_rst(self, submodule, module_name, path):
        filename = os.path.join(path, f"{submodule}.rst")
        content = (
            self.create_header(submodule) +
            self.create_automodule_directive(module_name, submodule)
        )
        self.write_to_file(filename, content)
        return filename

    def generate_rst_for_submodules(self, module):
        if not hasattr(module, "__all__"):
            return []

        module_name = module.__name__.replace("openstix.", "")
        path = os.path.join(self.output_dir, "library", module_name)
        os.makedirs(path, exist_ok=True)

        return [self.generate_rst(submodule, module.__name__, path) for submodule in module.__all__]

    def create_toctree_entry(self, file):
        return os.path.relpath(file, self.output_dir).replace(os.sep, '/')

    def generate_library_rst(self, generated_files):
        # Initialize sections
        sections = {'Objects': [], 'Extensions': [], 'Properties': []}
        
        # Populate sections
        for file in generated_files:
            if "objects" in file:
                sections['Objects'].append(file)
            elif "extensions" in file:
                sections['Extensions'].append(file)
            # Add more conditions as needed for 'Properties' or other sections
        
        # Write toctrees for sections
        for section, files in sections.items():
            if files:
                toctree_entries = "\n   ".join(self.create_toctree_entry(file) for file in files)
                toctree_content = TOCTREE_TEMPLATE.format(caption=section, entries=toctree_entries)
                section_filename = os.path.join(self.output_dir, "library", f"{section.lower()}.rst")
                self.write_to_file(section_filename, toctree_content)

    def run(self):
        modules = [definitions, objects, extensions]
        generated_files = []
        
        for module in modules:
            rst_files = self.generate_rst_for_submodules(module)
            generated_files.extend(rst_files)

        # Generate the library RST that includes the toctrees
        self.generate_library_rst(generated_files)

if __name__ == "__main__":
    rst_generator = RSTGenerator()
    rst_generator.run()
