// function copyToClipboard(elementId) {

//     // Create a "hidden" input
//     var aux = document.createElement("input");
  
//     // Assign it the value of the specified element
//     aux.setAttribute("value", document.getElementById(elementId).innerHTML);
  
//     // Append it to the body
//     document.body.appendChild(aux);
  
//     // Highlight its content
//     aux.select();
  
//     // Copy the highlighted text
//     document.execCommand("copy");
  
//     // Remove it from the body
//     document.body.removeChild(aux);

//     // display status
//     console.log('Copied')
  
//   }

console.log('starting');

const copyBtns = [...document.getElementsByClassName('copy-btn')]
console.log('copy btn pressed.');

let previous = null;

copyBtns.forEach(btn => btn.addEventListener('click', () => {
  console.log('clicked');
  const link = btn.getAttribute('data-link')
  // console.log(link);
  navigator.clipboard.writeText(link)
  btn.textContent = "Copied";

  if (previous) {
    previous.textContent = "Copy";
  }
  previous = btn

}))