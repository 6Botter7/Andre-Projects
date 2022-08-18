export class CvForm extends HTMLElement {

    async connectedCallback() {
        this.innerHTML = await fetch(import.meta.url.replace(".js", ".html")).then(result => result.text());

        this.mouseClickHandler = this.mouseClick.bind(this);

        this.addEventListener("click", this.mouseClickHandler);

        requestAnimationFrame(() => {

        })

    }

    async disconnectedCallback() {
        this.removeEventListener("click", this.mouseDownHandler);
        this.mouseDownHandler = null;
    }

    async mouseClick(event) {
         
        // console.log(this.querySelector(".app-form-control").value)
        // console.log(event.target)
        if (event.target.matches(".app-form-button")) {
            const fullName = this.querySelector("#fullName").value;
            const email = this.querySelector("#email").value;
            const contactNumber = this.querySelector("#contactNumber").value;
            const message = this.querySelector("#message").value;
            const details = `Your name: ${fullName}, email: ${email}, contact number: ${contactNumber} and your messsage: ${message}`
            alert("Your form has been 'submitted'" + details)

            // const x = 200;
            // const y = 100;
            // // let position = event.target
            // event.target.style.transform = `translate( ${x}px, ${y}px) scale(2) rotate(360deg)`;
            // event.target.style.background = "#0276C2";
        }
    }


}

// cv1 = new Cv1();


customElements.define("cv-form", CvForm);