const API = process.env.REACT_APP_API_GATEWAY

const GET = async (query_string) => {
    var api = `${API}${query_string}`
    
    return await fetch(api).then((response) => {return response.json()})
}

const POST = async (api_path, payload) =>{
    return await fetch(api_path, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(payload)
    }).then((response) => {return response.json})
}

const getLEDStripColour = (cabinet_id, strip_id) => {
    var api = `ledStatus?cabinet=${cabinet_id}&strip=${strip_id}`
    return GET(api)
}

const handleChangeComplete = (state, cabinet_id) => {
    var api = `${API}updateCabinet`
    var payload = {
        ...state,
        cabinet_id: cabinet_id
    }
    return POST(api, payload)
};

export {
    getLEDStripColour,
    handleChangeComplete
}