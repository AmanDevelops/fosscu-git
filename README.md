# 🚀FOSSCU-Git

This project is a Django-based implementation of a website for the Free and Open-Source Software Community United (FOSSCU). It integrates HTML and CSS assets from [JiyaGupta-cs/fosscu-git](https://github.com/JiyaGupta-cs/fosscu-git) into a Django framework solving critical problem of repeated request in its base version.

## ✨Features

- **Django Framework**: Utilizes Django for backend development.
- **HTML and CSS Integration**: Incorporates frontend assets from the original repository.
- **Modular Structure**: Organized into apps such as `home` and `member` for scalability.

## 📋Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django
- Git

## 🛠️Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/AmanDevelops/fosscu-git.git
   cd fosscu-git
   ```

2. **Set Up a Virtual Environment** (Optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

## 🏗️Project Structure

- `fosscu_git/`: Main project directory containing settings and configurations.
- `home/`: App managing the homepage and related views.
- `member/`: App handling member-related functionalities.
- `templates/`: Directory for HTML templates.
- `static/`: Directory for static assets like CSS and JavaScript files.

## 🤝Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**: Click on the 'Fork' button at the top right of this page.
2. **Clone Your Fork**:

   ```bash
   git clone https://github.com/your-username/fosscu-git.git
   cd fosscu-git
   ```

3. **Create a New Branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**.
5. **Commit Your Changes**:

   ```bash
   git add .
   git commit -m "Add your commit message"
   ```

6. **Push to Your Fork**:

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Submit a Pull Request**: Navigate to the original repository and click on 'New Pull Request'.


## 🙌Acknowledgements

- [JiyaGupta-cs/fosscu-git](https://github.com/JiyaGupta-cs/fosscu-git) for the original HTML and CSS assets.
- The FOSSCU community for their continuous support and contributions.

---

