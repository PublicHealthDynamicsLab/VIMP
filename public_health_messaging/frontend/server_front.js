
function arrayToList(array) {
    // https://stackoverflow.com/questions/55766543/turn-array-into-list-with-javascript
    let list = [null,null,null,null,null,null,null,null,null]
    for (i of array) {
        list[i] = array[i]
    }
    return list
}

window.onload = function() {
    var id = 0;
    console.log(id);
    getDropdowns()
    //startLoop();
    document.getElementById("generate-button").onclick=prompt

    vacc=document.getElementById("vaccine")
    for (child in vacc.children) {
        child = vacc.children[child]
        if (child.tagName == "BUTTON") {
            child.onclick = vaccChoose
        } 
    }
}

function vaccChoose() {
    vacc=document.getElementById("vaccine")
    deselect = false

    for (i in event.target.classList) {
        if (event.target.classList[i] == "selected") {
            deselect = true
        }
    }

    for (child in vacc.children) {
        child = vacc.children[child]
        if (child.tagName == "BUTTON") {
            child.classList=["vac-button"]
        }
    }
    if (!deselect) {
        event.target.classList.add("selected")
    }
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
        //new_el.classList.add()

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
    for (child in childs) {
        child = childs[child]
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
    body = JSON.stringify({
      title: "prompt",
      text: document.getElementById("prompt").value,
      vacc: getVacc(),
      filters: getFilters()
    })
    console.log(body)
    fetch(document.URL, {
      method: "POST",body: body, headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
    }).then((response) => response.json())
    .then(llmFiller)
}

function llmFiller(response) {
    console.log(response)
    document.getElementById("generationed-text").textContent=response["content"]
}


function getVacc() {
    vaccs=document.getElementsByClassName("vac-button");
    selected = "all"
    for (vacc of vaccs) {
        //vacc=vaccs[i]


        for (i in vacc.classList) {
            if (vacc.classList[i] == "selected") {
                selected = vacc.textContent
            }
        }
    }
    console.log(selected)
    return vacc.textContent
}

function getFilters() {
    filters = {}
    for (dropdown of document.getElementsByClassName("dropdowns")) {
        drop_id = dropdown.id
        dropdownl = []
        for (select of dropdown.children) {
            if (!select.hidden && select.tagName == "DIV") {
                for (label of select.children) {
                    if (label.tagName == "INPUT" && label.checked) {
                        dropdownl.push(label.id)
                    } else {
                        console.log(label.tagName)
                    }
                }
            }
        }

        if (dropdownl.length > 0){
            filters[drop_id]= dropdownl
        }
    }
    console.log(filters)
    //return {0:[0,1,2,3]}
    return filters
}