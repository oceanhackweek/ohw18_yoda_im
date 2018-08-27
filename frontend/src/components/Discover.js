import React from 'react'
import { push } from 'connected-react-router'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import {
  fetchParameters
} from '../actions/discover'
import Button from 'antd/lib/button'
import Input from 'antd/lib/input'
import '../css/Discover.css';

const Search = Input.Search;

const Discover = props => (
    <div>
        <h2>Products</h2>
        <Button onClick={props.fetchParameters} disabled={props.isFetching}>Get All Parameters</Button>
        <Search
            placeholder="input search text"
            onSearch={value => console.log(value)}
            style={{ width: 200 }}
        />
        <ul style={{ overflow: 'scroll', height: 400 }}>
            {props.products.map((param, i) => <li key={i}>{param}</li>)}
        </ul>
    </div>
)

const mapStateToProps = ({ parameters }) => ({
    products: parameters.products,
    isFetching: parameters.isFetching
  })
  
  const mapDispatchToProps = dispatch => bindActionCreators({
    fetchParameters
  }, dispatch)

export default connect(
    mapStateToProps,
    mapDispatchToProps
  )(Discover)