/* The following types out the name at the top of the website */
window.addEventListener("DOMContentLoaded", function() {
  const text = "Trevor Seestedt";
  const speed = 250; 
  let i = 0;
  const element = document.getElementById("site-title-typer");

  function typeWriter() {
    if (i < text.length) {
      element.textContent += text.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    }
  }

  typeWriter();
});


/* The following script open a new tab for my GitHub and Linkedin */
function linkedinNewTab() {
  window.open('https://www.linkedin.com/in/trevor-seestedt/', '_blank');
}

function githubNewTab() {
  window.open('https://github.com/TrevorSeestedt', '_blank');
}