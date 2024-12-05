let parcelopindex=document.querySelector("#parcel_icon");
let rideopindex=document.querySelector("#ride_icon");
let flyopindex=document.querySelector("#fly_icon");
let locsecindex=document.querySelector(".loc");
let parcelsecindex=document.querySelector(".parcel");
let flysecindex=document.querySelector(".fly");

parcelopindex.addEventListener("click",()=>{
    parcelopindex.querySelector("i").style.backgroundColor="rgb(98, 146, 250)";
    rideopindex.querySelector("i").style.backgroundColor="white";
    flyopindex.querySelector("i").style.backgroundColor="white";
    parcelopindex.querySelector("i").style.color="black";
    rideopindex.querySelector("i").style.color="#525252";
    locsecindex.classList.add("hide");
    flyopindex.querySelector("i").style.color="#525252";
    parcelsecindex.classList.remove("hide");
    document.querySelector(".map").classList.add("hide");
    flysecindex.classList.add("hide");
    document.querySelector(".ride_text").
    innerText="Track your parcel to get detailed update";
})

rideopindex.addEventListener("click",()=>{
    rideopindex.querySelector("i").style.backgroundColor="rgb(98, 146, 250)";
    parcelopindex.querySelector("i").style.backgroundColor="white";
    flyopindex.querySelector("i").style.backgroundColor="white";
    rideopindex.querySelector("i").style.color="black";
    flyopindex.querySelector("i").style.color="#525252";
    parcelopindex.querySelector("i").style.color="#525252";
    locsecindex.classList.remove("hide");
    parcelsecindex.classList.add("hide");
    document.querySelector(".map").classList.remove("hide");
    flysecindex.classList.add("hide");
    document.querySelector(".ride_text").innerText="Go anywhere with SumTransit";
    document.querySelector(".map").style.height="450px";
})

flyopindex.addEventListener("click",()=>{
    flyopindex.querySelector("i").style.backgroundColor="rgb(98, 146, 250)";
    rideopindex.querySelector("i").style.backgroundColor="white";
    parcelopindex.querySelector("i").style.backgroundColor="white";
    flyopindex.querySelector("i").style.color="black";
    rideopindex.querySelector("i").style.color="#525252";
    parcelopindex.querySelector("i").style.color="#525252";
    locsecindex.classList.add("hide");
    parcelsecindex.classList.add("hide");
    flysecindex.classList.remove("hide");
    document.querySelector(".map").classList.remove("hide");
    document.querySelector(".ride_text").innerText="Fly anywhere with SumTransit";
    document.querySelector(".map").style.height="550px";
})

    



