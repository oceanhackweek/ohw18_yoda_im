import { combineReducers } from 'redux'
import counter from './counter'
import { parameters } from './discover'


export default combineReducers({
    counter,
    parameters
})