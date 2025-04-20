// auth.js

// Function to store the access token in local storage
export const login = (token) => {
  localStorage.setItem("access_token", token); // Store token in local storage
};

// Function to check if the user is logged in (by checking the presence of the token in local storage)
export const isAuthenticated = () => {
  return localStorage.getItem("access_token") !== null; // Check if token exists in local storage
};

// Function to log the user out by clearing the stored token
export const logout = () => {
  localStorage.removeItem("access_token"); // Remove token from local storage
};

// Function to get the stored access token
export const getToken = () => {
  return localStorage.getItem("access_token"); // Retrieve the token from local storage
};
