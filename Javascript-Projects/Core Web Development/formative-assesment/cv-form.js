export class CvForm extends HTMLElement {
    
    async connectedCallback() {
        this.innerHTML = await fetch(import.meta.url.replace(".js", ".html")).then(result => result.text());
        console.log("Connected");


        requestAnimationFrame(() => {
            console.log("Connected 2");
        }
        )
    }


    disconnectedCallback() {


    }
    
    
 }

// cv1 = new Cv1();


customElements.define("cv-form" , CvForm);