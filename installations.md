# Wiki

## Quick Start Step By Step



### 2. Start building software in one command:

- **Build Your Software:** Use the following command to initiate the building of your software:

   ```
   python app.py
   ```

### 3. Check the code

- html, css and js currently are in one place.

    ```commandline
    ├── static/ #This directory is typically used for storing static assets like CSS, JavaScript, and images.
    ├── templates/ #This directory contains HTML templates for the web pages.
    │   ├── 404.html  #The error page displayed when a page is not found.
    │   ├── index.html # The main landing page of the application.
    │   ├── result.html #The page that displays the result genrated by llm
    ├── apis.py #This file contains API key and model initailzation.
    ├── app.py #The main application file initializes and runs the web server.
    ├── vercel.json #Configuration file for deploying the project on Vercel
    ├── wiki.md #Documentation file for the project
    └── requirements.txt #A file listing the Python dependencies needed to run the project.
    ```
    
- Usually, you just need to install requirements and run app.py to use your software
    ```commandline
    cd ResumeXpert
    pip install -r requirements.txt
    python app.py
    ```



