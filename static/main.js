console.log('hello world')
console.log(document)

const test = document.getElementById('test')
console.log(test)

setTimeout(()=>{
    test.textContent = "How are you doing?"
}, 2000)