const createOdometer=(el,value)=>{
    const odometer=new Odometer({
        el:el,
        value:0,
    });
    const options={
        threshold:[0,0.9]
    };
    let hasRun=false;
    const callback=(entries,observer)=>{
        entries.forEach(entry=>{
            if(entry.isIntersecting){
                if(!hasRun){
                     odometer.update(value);
                     hasRun=true;   
                }
            }
        })
    }
    const observer=new IntersectionObserver(callback,options)
    observer.observe(el)

}
const studentsOdometer=document.querySelector(".students-odometer");
createOdometer(studentsOdometer,1048,)
const teachersOdometer=document.querySelector(".teachers-odometer");
createOdometer(teachersOdometer,430)
const experianceOdometer=document.querySelector(".experiance-odometer");
createOdometer(experianceOdometer,10)
