
window.onload = function() {
    var id = 0;
    console.log(id);
    getDropdowns()
    //startLoop();
    document.getElementById("generate-button").onclick=prompt
}


function getDropdowns() {
    
    fetch(document.URL, {
      method: "POST",body: JSON.stringify({
      title: "dropdowns",
    }), headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
    }).then((response) => response.json())
    .then(handleDrops)
}

function handleDrops(resp_json) {
    console.log("Handling drops")
    filter_node=  document.getElementById("filters")
    console.log(filter_node)
    console.log(resp_json["Contents"])
    for (title in resp_json["Contents"]) {
        new_div = document.createElement("div");
        new_div.classList.add("dropdowns")
        new_div.id = title



        new_el = document.createElement("button");
        new_el.onclick = hideSiblings;
        new_el.innerText = title
        new_el.title = title
        new_el.classList.add()

        new_div.appendChild(new_el)

        for (desc in resp_json["Contents"][title]) {
            desc = resp_json["Contents"][title][desc]
            mini_div= document.createElement("div")
            new_el = document.createElement("input");
            new_el.type = "checkbox"
            new_el.id = desc

            new_desc = document.createElement("label");
            new_desc.innerText = desc
            new_desc.for = desc
            mini_div.appendChild(new_el);
            mini_div.appendChild(new_desc);
            mini_div.hidden = true
            new_div.appendChild(mini_div)
        }

        filter_node.appendChild(new_div)
    }
}

function hideSiblings() {
    console.log(event.target)
    childs=event.target.parentElement.children
    console.log(childs)
    for (child in childs) {
        child = childs[child]
        console.log(child.tagName)
        if (child.tagName == "DIV") {
            console.log(child.id)
            if (child.hidden) {
                child.hidden=false
            } else {
                child.hidden=true
            }
            for (checkbox in child.children) {
                checkbox=child.children[checkbox]
                if (checkbox.tagName == "INPUT") {
                    checkbox.checked = false
                }
            }
        }
    }
}

function prompt() {
    fetch(document.URL, {
      method: "POST",body: JSON.stringify({
      title: "prompt",
      text: document.getElementById("prompt").value
    }), headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
    }).then((response) => response.json())
    .then(llmFiller)
}

function llmFiller(response) {
    console.log(response)
    document.getElementById("generationed-text").textContent=response["content"]
}