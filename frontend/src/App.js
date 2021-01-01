import { BrowserRouter as Router, Route, Switch, Redirect } from "react-router-dom";
import Login from './views/login/Login'
import Home from './views/home/Home'
function App() {
  return (
    <Router>
      <Switch>
        <Redirect from="/" to="login" exact />
        <Route path="/login" component={Login} exact />
        <Route path="/*" component={Home} exact />
      </Switch>
    </Router>
  );
}

export default App;
