---
layout: default
page_title: About
permalink: /about/
---

# A bit about me

I'm Pablo Martín Calvo, and this website showcases the projects I’ve worked on in the past.

I transitioned from over 8 years as a teacher and instructional designer into data engineering. My interest in data
began during my work at [IIEP-UNESCO](https://www.iiep.unesco.org/en/)
on [Education Sector Plans](https://policytoolbox.iiep.unesco.org/glossary/education-sector-plan-esp/)  where I realized
the impact of data-driven decisions. This motivated me to enhance my technical skills, leading me to complete a Data
Analyst program at [Wild Code School](https://www.wildcodeschool.com/) in Paris.

After 10 months as Data Analyst
at [Delta - SamuSocial de Paris](https://www.samusocial.paris/delta-gestion-de-loffre-hoteliere-vocation-sociale-en-idf),
I discovered a passion for data engineering. I returned to [Wild Code School](https://www.wildcodeschool.com/) to train
specifically in Data Engineering.

Since then, I've developed strong skills in data pipelines, ETL processes, and database management. This portfolio
reflects how I have evolved as a data professional and highlights the skills I bring to the table today.

## My tech stack

Python, SQL, Docker, Airflow, Kafka, Kubernetes, Terraform, AWS, GCP, Dataiku, and more.

Explore my projects to see some of the things I'm capable of building and deploying!

## Connect with me:

<a href="{{ site.linkedin_profile }}" target="_blank">
  <img src="https://store-images.s-microsoft.com/image/apps.31120.9007199266245564.44dc7699-748d-4c34-ba5e-d04eb48f7960.bc4172bd-63f0-455a-9acd-5457f44e4473" alt="LinkedIn Profile"> LinkedIn Profile
</a>

<a href="{{ site.github.owner_url }}" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/180px-GitHub_Invertocat_Logo.svg.png" alt="GitHub Profile"> GitHub Profile
</a>

<a href="mailto:{{ site.email }}" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/1200px-Gmail_icon_%282020%29.svg.png" alt="Email"> Email
</a>

<div>
    <label for="languageSelect">Choose your language:</label>
    <select id="languageSelect" style="margin: 0 1em 0 0;" onchange="updateResumeLink() ">
        <option value="en">English</option>
        <option value="fr">French</option>
        <option value="es">Spanish</option>
        <!-- Add more options for other languages if needed -->
    </select>

    <a id="resumeLink" href="/assets/cv/CV Data Engineer - Pablo Martín Calvo - en.pdf" target="_blank">
        Download Resume
    </a>

</div>

<script>
    function updateResumeLink() {
        const languageSelect = document.getElementById("languageSelect");
        const selectedLanguage = languageSelect.value;
        const resumeLink = document.getElementById("resumeLink");
        const resumeImage = document.getElementById("resumeImage");

        // Update the resume link based on the selected language
        if (selectedLanguage === "en") {
            resumeLink.href = "/assets/cv/CV Data Engineer - Pablo Martín Calvo - en.pdf";
            resumeImage.src = "/assets/images/CV Data Engineer - Pablo Martín Calvo.jpg"; // Update to specific image for English
        } else if (selectedLanguage === "fr") {
            resumeLink.href = "/assets/cv/CV Data Engineer - Pablo Martín Calvo - fr.pdf";
            resumeImage.src = "/assets/images/CV Data Engineer - Pablo Martín Calvo.jpg"; // Update to specific image for French
        } else if (selectedLanguage === "es") {
            resumeLink.href = "/assets/cv/CV Data Engineer - Pablo Martín Calvo - es.pdf";
            resumeImage.src = "/assets/images/CV Data Engineer - Pablo Martín Calvo.jpg"; // Update to specific image for Spanish
        } // Add more languages as needed
    }
</script>


<div class="button-wrapper">
  <a href='{{ "/" | relative_url }}' class="in-body-btn">Back to Home</a>
</div>