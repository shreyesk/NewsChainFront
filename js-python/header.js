class Header extends HTMLElement {
    constructor() {
      super();
    }


    connectedCallback(){
        this.innerHTML = `
            <header>
                <h1><img src= "/images/newsdraft.PNG" alt="Logo"></h1>
                <nav>
                    <ul>
                        <li><a href="/index.html"><span>Home</span></a></li>
                        <li><a href="/html/submit.html"><span>Submit an Article</span></a></li>
                    </ul>
                </nav>
            </header>
            `
    }
}

customElements.define('header-component', Header);