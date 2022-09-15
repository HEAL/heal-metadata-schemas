# convert the md file for investigators to pdf for easy download and viewing offline
# pandoc must be installed on system as prerequisite

import os
import subprocess


repo_path = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas"

input_md = os.path.join(repo_path,"for-investigators-how-to","study-level-metadata-fields","study-metadata-schema-for-humans.md")
output_pdf = os.path.join(repo_path,"for-investigators-how-to","study-level-metadata-fields","study-metadata-schema-for-humans.pdf")


subprocess.run(["pandoc",
                input_md,
                "-o",
                output_pdf])
