import * as actionTypes from '../utils/actionTypes'

export const parameters = (
    state = {
        products: [],
        receivedAt: Date.now(),
        isFetching: false
    }, action
) => {
    switch(action.type) {
        case actionTypes.FETCH_PARAMETERS:
            return {
                ...state,
                isFetching: true
            }
        case actionTypes.RECEIVE_PARAMETERS:
            return {
                ...state,
                isFetching: !state.isFetching,
                products: action.products
            }
        case actionTypes.FILTER_PARAMETERS:
            return {
                ...state,
                products: state.products
            }
        default:
            return state
    }
}