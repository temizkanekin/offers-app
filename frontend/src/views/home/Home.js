import { Route, Switch } from "react-router-dom";
import Toolbar from '../../components/toolbar/Toolbar'
import Offers from '../offers/Offers'
import OfferDetail from '../offer-detail/OfferDetail'
import './Home.css'
const Home = () => {
    return (
        <>
            <Toolbar />
            <main className="content">
                <Switch>
                    <Route path="/offers" component={Offers} exact />
                    <Route path="/offers/:recipient_id" component={OfferDetail} exact />
                </Switch>
            </main>
        </>
    )
}

export default Home;