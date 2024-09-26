import yaml
import sys


def load_yaml(yaml_file):
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)


def replace_placeholders(latex_template, data, language_code):
    for key, values in data.items():
        placeholder = f"{{{{{key}}}}}"
        if language_code in values:
            latex_template = latex_template.replace(placeholder, values[language_code])
    return latex_template


def main():
    # Check if a language code is passed as an argument
    if len(sys.argv) < 2:
        print("Please provide a language code (e.g., 'en', 'es', 'fr')")
        sys.exit(1)

    language_code = sys.argv[1]

    # Load YAML file
    data = load_yaml('cv_content.yml')

    # Load the LaTeX template
    with open('template.tex', 'r') as file:
        latex_template = file.read()

    # Replace placeholders with YAML content
    updated_latex = replace_placeholders(latex_template, data, language_code)

    # Save the updated LaTeX file
    with open('output.tex', 'w') as file:
        file.write(updated_latex)


if __name__ == '__main__':
    main()
