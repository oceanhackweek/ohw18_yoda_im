import React from 'react';
import { Route, Link } from 'react-router-dom'
import Home from './components/Home'
import About from './components/About'
import Discover from './components/Discover'

const App = () => (
  <div>
    <header>
      <Link to="/">Home</Link>
      <Link to="/about-us">About</Link>
    </header>

    <main>
      <Route exact path="/" component={Discover} />
      <Route exact path="/about-us" component={About} />
    </main>
  </div>
)

export default App;
