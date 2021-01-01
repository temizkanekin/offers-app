import React from "react"
import axios from "axios";
import Cookies from 'universal-cookie';
import { useHistory } from 'react-router-dom';

import './Offers.css'
const cookies = new Cookies()

const Offers = () => {
    const [items, setItems] = React.useState([])
    const [page, setPage] = React.useState(1)
    const [applyFilter, setApplyFilter] = React.useState(false)
    const history = useHistory()

    const getOffers = (page) => {
        axios.get(`/api/offers?page=${page}&per_page=25`, { headers: { 'Authorization': `Bearer ${cookies.get("token", { path: '/' })}` } })
            .then(res => {
                setItems([...items, ...res.data.items])
                setPage(page + 1)
            })
            .catch(er => console.log(er))
    }

    React.useEffect(() => {
        getOffers(page)
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

    const handleOfferDetail = (item) => (e) => {
        history.push(`/offers/${item.recipient_id}`, { item })
    }

    const handleScroll = (e) => {
        let element = e.target
        if (element.scrollHeight - element.scrollTop === element.clientHeight) {
            getOffers(page)
        }
    }

    const filteredItems = applyFilter ? items.filter(item => item.transaction_type === "deposit" && item.amount > 50000) : items

    return (
        <div className="offers-container">
            <button className="btn btn-primary w-25" onClick={() => setApplyFilter(!applyFilter)}>{!applyFilter ? "Apply Filter" : "Cancel Filter"}</button>
            <div className="offers" onScroll={handleScroll}>
                {
                    filteredItems.map((item, i) =>
                        <div key={i} className="card" style={{ width: "250px", height: "220px", margin: "10px" }}>
                            <div className="card-body">
                                <h4 className="card-title">{item.amount}</h4>
                                <div className="card-text">
                                    <ul className="list-unstyled">
                                        <li>transaction_type: {item.transaction_type}</li>
                                        <li>vade: {item.vade}</li>
                                        <li>interest: {item.interest}</li>
                                        <li>time_limit: {item.time_limit}</li>
                                    </ul>
                                </div>
                                <button onClick={handleOfferDetail(item)} className="btn btn-link p-0">Go to offer detail</button>
                            </div>
                        </div>
                    )
                }
            </div>
            {/**Infinite scroll handler for lower per page items */}
            {
                items.length > 0 && items.length < 25 && <button className="btn btn-primary" onClick={() => getOffers(page)}>Show More</button>
            }
        </div>
    )
}
export default Offers;