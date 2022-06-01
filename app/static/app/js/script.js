const searchBtn = document.getElementById("search-btn")
const urlInput = document.getElementById("url-input")
const form = document.getElementById("form")
const title = document.getElementById("title")

urlInput.addEventListener("input", (e)=>{
    if (e.target.value.slice(0, 9) == "( '-' ) ?")  {
        e.target.value = e.target.value.slice(9)
    }
})

urlInput.addEventListener("click", (e)=>{
    e.target.value = ""
})

searchBtn.addEventListener("click", (e)=>{
    if (verify_url()) {
        // form.setAttribute("action", "/search/")
        e.target.focus()
        e.target.innerHTML = '<i class="fa fa-circle-o-notch fa-spin loading-icon"></i>';
    } else {
        urlInput.value = "( '-' ) ?"
        
    }
})

function verify_url(){
    let input = urlInput.value
    if (input == "" || input==" " || !isValidHttpUrl(input)){
        return false
    }
    return true
}

function isValidHttpUrl(string) {
    let url;
    
    try {
      url = new URL(string);
    } catch (_) {
      return false;  
    }
  
    return url.protocol === "http:" || url.protocol === "https:";
  }