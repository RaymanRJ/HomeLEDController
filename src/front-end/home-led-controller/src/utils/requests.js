const API = process.env.REACT_APP_API_GATEWAY

const getInitCabinet = (cabinetId) =>{

    var resp;

    var api = `${API}cabinetStatus/${cabinetId}`
    fetch(api, {mode: 'no-cors'})
        .then((response) => response.json())
        .then((json) => resp = json)
        .then(() => console.log(resp))
    return resp;
}

export default getInitCabinet