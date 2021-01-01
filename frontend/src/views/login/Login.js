import React from "react"
import './Login.css'
import axios from "axios";
import Cookies from 'universal-cookie';

const cookies = new Cookies()

const Login = ({ history }) => {
    const [username, setUsername] = React.useState("")
    const [password, setPassword] = React.useState("")
    const [error, setError] = React.useState(undefined)
    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post("/api/login", {}, { auth: { username: username, password: password } })
            .then(res => {
                cookies.set("token", res.data.token, { path: '/' })
                history.push("/offers")
            })
            .catch(er => setError(er.response.data.error || er.response.data))
    }
    return (
        <div className="login-form-container">
            <form className="login-form" onSubmit={handleSubmit}>
                {
                    error &&
                    <div className="toast fade show" role="alert" aria-live="assertive" aria-atomic="true" style={{ position: "absolute", top: "15px" }}>
                        <button onClick={() => setError(undefined)} type="button" className="ml-2 mb-1 close" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                        <div className="toast-body">
                            {error}
                        </div>
                    </div>
                }
                <div className="form-group">
                    <label htmlFor="username">User Name</label>
                    <input className="form-control" name="username" type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password</label>
                    <input className="form-control" name="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                </div>
                <input className="btn btn-light" disabled={!username || !password} type="submit" value="Oturum aç"></input>
            </form>
        </div>
    )
}

export default Login