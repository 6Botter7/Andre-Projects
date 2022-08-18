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
        if (event.target.matches("#sendBtn")) {
            const fullName = this.querySelector("#fullName").value;
            const email = this.querySelector("#email").value;
            const contactNumber = this.querySelector("#contactNumber").value;
            const message = this.querySelector("#message").value;
            const details = `Your name: ${fullName}, email: ${email}, contact number: ${contactNumber} and your messsage: ${message}`
            alert("Your form has been 'submitted'" + details)
        }

        if (event.target.matches("#cancelBtn")) {
            alert("You Cancelled the form!")
        }
    }


}

customElements.define("cv-form", CvForm);