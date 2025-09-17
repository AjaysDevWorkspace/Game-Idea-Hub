const container = document.createElement('div');
const h1 = document.createElement('h1');
const btn = document.createElement('button');
btn.append('Click Me!');

document.body.insertAdjacentElement('afterbegin', container);
container.insertAdjacentElement('beforeend', btn);
container.insertAdjacentElement('afterbegin', h1);
h1.append('rgb(255 ,255 ,255)')

container.style.textAlign = 'center';

function ranColor(){
    let a = Math.floor(Math.random()*255 + 1);
    let b = Math.floor(Math.random()*255 + 1);
    let c = Math.floor(Math.random()*255 + 1);
    
    const ranColor = `rgb(${a} ,${b}, ${c})`;
    document.body.style.backgroundColor = `${ranColor}`;
    h1.innerText = `${ranColor}`;
    
    // for(let i = 0; i<100;i++){

    //     let a = Math.floor(Math.random()*255 + 1);
    //     let b = Math.floor(Math.random()*255 + 1);
    //     let c = Math.floor(Math.random()*255 + 1);
        
    //     const ranColor = `rgb(${a} ,${b}, ${c})`;
    //     document.body.style.backgroundColor = `${ranColor}`;
    //     h1.innerText = `${ranColor}`;
    //     console.log(i);
    //     setInterval(()=>{
    //         console.log('loop completed')
    //     },1000)
    // }
}

btn.addEventListener('click', ranColor);