// simple interactive behaviors for Option C
function animateStar(btn){
// add a quick pop animation (Animate.css class used)
btn.classList.remove('animate__pulse');
btn.classList.add('animate__tada');
setTimeout(()=> btn.classList.remove('animate__tada'), 800);


// optional: increment the visible rating temporarily (demo only)
const tr = btn.closest('tr');
const ratingSpan = tr.querySelector('.rating');
let val = parseFloat(ratingSpan.textContent) || 0;
val = Math.min(5, (val + 0.1));
ratingSpan.textContent = val.toFixed(2);
}


// small clickable ripple for CTA (demo)
document.addEventListener('click', (e)=>{
if(e.target.classList.contains('cta-btn')){
e.target.classList.add('animate__heartBeat');
setTimeout(()=> e.target.classList.remove('animate__heartBeat'), 900);
}
});