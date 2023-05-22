let toggle=true;
gsap.registerPlugin(ScrollTrigger)
gsap.utils.toArray(".row").forEach((section, index) => {
    const [x, xEnd] =
        index % 2
            ? ["20%", ((section.scrollWidth - section.offsetWidth) / 2) * -2]
            : [(section.scrollWidth * -1) / 4, "10%"];

    gsap.fromTo(
        section,
        { x },
        {
            x: xEnd,
            scrollTrigger: {
                trigger: section,
                scrub: 0.1,
            }
        }
    );
})

document.getElementById("menubutton").addEventListener("click",()=>{
    let element = document.getElementById("navbar")
    if(toggle){
        element.classList.add("nav2");
        element.classList.remove("nav");
    }else{
        element.classList.add("nav");
        element.classList.remove("nav2");
    }
    toggle=!toggle;

    console.log("clicked 1");

})