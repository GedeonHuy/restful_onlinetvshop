import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";
import ProductTable from "./ProductTable";
import UserTable from "./UserTable";

const Brand = () => (
  <DataProvider endpoint="api/brand/" 
                render={data => <Table data={data} />} />
);
const brandWrapper = document.getElementById("brands");
brandWrapper ? ReactDOM.render(<Brand />, brandWrapper) : null;

const Product = () => (
  <DataProvider endpoint="api/product/" 
                render={data => <Table data={data} />} />
);
const productWrapper = document.getElementById("products");
productWrapper ? ReactDOM.render(<Product />, productWrapper) : null;

const User = () => (
  <DataProvider endpoint="api/user/" 
                render={data => <Table data={data} />} />
);
const userWrapper = document.getElementById("users");
userWrapper ? ReactDOM.render(<User />, userWrapper) : null;