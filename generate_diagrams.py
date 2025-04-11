#!/usr/bin/env python3

import os
import subprocess
import glob

def generate_diagrams():
    """Generate diagrams using PlantUML jar."""
    # Create diagrams directory if it doesn't exist
    if not os.path.exists('diagrams'):
        os.makedirs('diagrams')
    
    # Download PlantUML jar if not present
    plantuml_jar = "plantuml.jar"
    if not os.path.exists(plantuml_jar):
        print("Downloading PlantUML jar...")
        subprocess.run(["wget", "https://github.com/plantuml/plantuml/releases/download/v1.2023.13/plantuml-1.2023.13.jar", "-O", plantuml_jar])
    
    # Find all .puml files in the diagrams directory
    puml_files = glob.glob('diagrams/*.puml')
    
    print(f"Found {len(puml_files)} PlantUML files to process.")
    
    # Generate diagrams for each .puml file
    for puml_file in puml_files:
        base_name = os.path.splitext(os.path.basename(puml_file))[0]
        output_path = f"diagrams/{base_name}.png"
        
        print(f"Generating diagram for {puml_file}...")
        
        # Run PlantUML to generate the diagram
        subprocess.run(["java", "-jar", plantuml_jar, puml_file])
        
        print(f"Generated {output_path}")
    
    print("All diagrams have been generated.")

if __name__ == "__main__":
    generate_diagrams() 