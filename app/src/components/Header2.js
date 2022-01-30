import axios from "axios";

function Header(props) {

  function logMeOut() {
    axios({
      method: "POST",
      url: global.LOGOUT,
    })
    .then((response) => {
       props.token()
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

    return(
        <header>
        </header>
    )
}

export default Header;

