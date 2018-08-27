import * as actionTypes from '../utils/actionTypes'
import fetch from 'cross-fetch'

const SERVER_HOST = 'localhost'
const SERVER_PORT = 4567

export const receiveParameters = (json) => {
    return {
      type: actionTypes.RECEIVE_PARAMETERS,
      products: json,
      receivedAt: Date.now()
    }
  }

  function filterItems(query) {
    return fruits.filter(function(el) {
        return el.toLowerCase().indexOf(query.toLowerCase()) > -1;
    })
  }

export const filterItems = (query) => {
    return {
        type: actionTypes.FILTER_PARAMETERS,
        products: 
    }
}

export const fetchParameters = () => {
    return dispatch => {
        return fetch(`http://${SERVER_HOST}:${SERVER_PORT}/products`)
        .then(response => response.json())
        .then(json => dispatch(receiveParameters(json)))
    }
  }

export const filterParameters = (query) => {
    return dispatch => {
        return dispatch({
            type: actionTypes.FILTER_PARAMETERS
        })
    }
}