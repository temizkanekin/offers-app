import { withRouter } from 'react-router-dom';
const Toolbar = ({ location }) => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light" style={{ height: '60px' }}>
            <div className="collapse navbar-collapse">
                <ul className="navbar-nav m-auto mt-2 mt-lg-0">
                    <li className={`nav-item ${location.pathname.includes('offers') && "active"}`}>
                        <a className="nav-link lead" href="/offers">Offers</a>
                    </li>
                    {/* <li className={`nav-item ${location.pathname === '/filter' && "active"}`}>
                        <a className="nav-link lead" href="/filter">Filter</a>
                    </li> */}
                </ul>
            </div>
        </nav>
    )
}
export default withRouter(Toolbar);