standard_html = '<select class="form-select" name="shifr_choose" onchange="javascript:return onchangeShifr(this)"> <option value="0">Удалить</option><option value="caesar">Цезарь</option><option value="morse">Морзе</option></select>';
caesar_html = ' <input type="number" name="quantity" min="1" max="100" step="1" value="1">';
dict_shifrs =
{
    "0": "Удалить",
    "caesar": "Цезарь",
    "morse": "Морзе",
    "atbash": "Атбаш"
}

function caesar_shift(shifr)
{
    numberElement = document.createElement("input");
    numberElement.setAttribute('type', "number");
    numberElement.setAttribute('name', "shift");
    numberElement.setAttribute('min', "0");
    numberElement.setAttribute('max', "100");
    numberElement.setAttribute('step', "1");
    numberElement.setAttribute('value', "1");
    shifr.appendChild(numberElement);
}

function addShifr(choose="morse", not_first_b = true)
{
    const shifrFields = document.getElementById('shifrFields');
    const lastShifr = shifrFields.lastElementChild;
    const newShifr = document.createElement('div');
    newShifr.classList.add('shifrField');
    newShifr.style = "display: inline-block;";

    formElement = document.createElement("select");
    formElement.setAttribute('class',  "form-select");
    formElement.name = "shifr_choose";
    formElement.setAttribute('onchange', "javascript:return onchangeShifr(this)");

    for (shifr in dict_shifrs)
    {
        optionElement = document.createElement("option");
        optionElement.value = shifr;
        optionElement.text = dict_shifrs[shifr];
        formElement.appendChild(optionElement);
    }

    formElement.value = choose;
    newShifr.appendChild(formElement);

    if (choose == "caesar")
    {
        caesar_shift(newShifr);
    }

    if (lastShifr == null)
    {
        newShifr.id = 0;
    }
    else newShifr.id = +lastShifr.id + 1;

    shifrFields.appendChild(newShifr);

    return false;
}

function onchangeShifr(selector)
{
    id = selector.closest('div .shifrField').id;
    shifr = document.getElementById(id)
    if (selector.value == "0")
    {
      document.getElementById('shifrFields').removeChild(shifr);
      return false
    }

    else if (selector.value == "caesar")
    {
      caesar_shift(shifr);
    }
    else
    {
        listChild = shifr.getElementsByTagName("input");
        while (listChild.length > 0)
        {
            listChild[0].remove();
        }
    }
    return false;
}