// Mobile menu
const mb=document.getElementById('mb'),nav=document.getElementById('nav');
mb&&mb.addEventListener('click',()=>{const o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
// Mark affiliate links safely
document.querySelectorAll('a[data-aff]').forEach(a=>{a.rel='sponsored noopener noreferrer';a.target='_blank'});
// Contact form: set data-endpoint on the form to your Formspree/Getform URL
const f=document.getElementById('cf');
if(f)f.addEventListener('submit',async e=>{e.preventDefault();const s=document.getElementById('st'),u=f.dataset.endpoint;
 if(!u||u.includes('YOUR_')){s.textContent='Form not connected yet. Add your form endpoint in contact.html (see README).';return}
 try{const r=await fetch(u,{method:'POST',body:new FormData(f),headers:{Accept:'application/json'}});
 s.textContent=r.ok?'Thanks, your message was sent.':'Something went wrong. Please try again.';if(r.ok)f.reset()}catch{s.textContent='Network error. Please try again.'}});
