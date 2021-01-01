import { useHistory } from 'react-router-dom';

const OfferDetail = () => {
    const history = useHistory();
    const { item } = history.location.state || { recipient_id: "", amount: "", communication: "", interest: "", time_limit: "", total_amount: "", total_interest: "", transaction_type: "", vade: "" }
    return (
        <div className="m-auto d-flex flex-column">
            <dl className="dl-horizontal">
                <dt className="mb-2">Detail of the offer with recipient id: {item.recipient_id}</dt>
                <dd>Amount of the offer is: {item.amount}</dd>
                <dd>Communication of the offer is: {item.communication}</dd>
                <dd>Interest of the offer is: {item.interest}</dd>
                <dd>Time limit of the offer is: {item.time_limit}</dd>
                <dd>Total Amount of the offer is: {item.total_amount}</dd>
                <dd>Total Interest of the offer is: {item.total_interest}</dd>
                <dd>Transaction Type of the offer is: {item.transaction_type}</dd>
                <dd>Vade of the offer is: {item.vade}</dd>
            </dl>
            <button className="btn btn-secondary" onClick={() => history.goBack()}>Go Back</button>
        </div>
    )
}
export default OfferDetail