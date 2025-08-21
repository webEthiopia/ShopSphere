import Header from "../components/Header";
import Navbar from "../components/Navbar";
import React from "react";
import axios from "axios";

function ShopPage(){
  const [topSellers, setTopSellers] = React.useState([]);

  React.useEffect(() => {
    axios.get('http://192.168.0.156:8000/api/top-sellers/')
      .then((response) => {
        setTopSellers(response.data);
      })
  }, [])

  return (
    <>
      <div className="top">
        <Header />
        <Navbar />
      </div>
      <section className="topSellers">
        {topSellers.map((seller) => (
          <div key={seller.id} className="seller">
            <h2>{seller.name}</h2>
            <p>{seller.description}</p>
          </div>
        ))}
      </section>
    </>
  )
}

export default ShopPage;