# Mycelium API Server

In the heart of the digital realm, a seed of an idea sprouted - an idea that would mimic nature's intricate connections in an entirely new landscape. It was during the burgeoning days of the NFT revolution, a time when digital assets were beginning to claim their rightful place in the world. We, a small team of innovators, found our muse in the enthralling mycelial networks that span beneath the forest floors.

This unassuming life form, championed by renowned forester and author Peter Wohlleben in his book, "The Hidden Life of Trees," presents a sophisticated and interconnected web, teeming with communication and exchange - nature's internet. It was here that the inspiration for our NFT marketplace's API was born.

The serendipitous wordplay between ‘non-fungible’ and 'non-fungable’ token led to the inception of an API that encapsulates the essence of mycelium. Our API, akin to the mycelial networks, aims to connect digital creators and enthusiasts across the globe, fostering a vibrant ecosystem for the trade and exchange of unique, digital assets.

We looked to the mycelium not only for its symbolic representation of interconnection but also for its decentralization, its resilience, and its organic evolution. Thus, our API emerged, intertwining nature's wisdom with blockchain technology, to create a backend system that is as vibrant and dynamic as the mycelium that inspired it.

The Mycelium API Server is a robust backend system built using Python, Django, and PostgreSQL. It serves as the backbone for the [Mycelium NFT Minting Platform](https://myceliumnft.netlify.app/), handling user authentication, protected routes, and synchronization with the Alchemy API for blockchain connectivity.

## Features

- **JWT Authentication**: We use JSON Web Tokens (JWT) for secure user authentication, ensuring that user data is protected and sessions are managed efficiently.

- **Protected Routes**: Our API server includes a variety of protected routes, ensuring that only authenticated users can access certain data and functionalities.

- **Alchemy API Synchronization**: We synchronize our API with the Alchemy API, which allows us to connect our application directly to the blockchain for seamless NFT minting.

- **PostgreSQL Database**: We use PostgreSQL, a powerful, open-source object-relational database system, to manage and store our application data.

## Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/mycelium-api.git
```

2. **Set up your virtual environment**

Navigate to the project directory and set up your virtual environment:

```bash
cd mycelium-api
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip3 install -r requirements.txt
```

4. **Start the server**

```bash
python3 manage.py runserver
```

The server will start running on `http://localhost:8000`

## Deployed Site

Our API server is deployed and can be accessed [here](https://nft-mint-api-824f9dc02cba.herokuapp.com/)

## Frontend Repository and Deployment

Our frontend repository can be found at [this link](https://github.com/lst68868/mycelium) and the deployed site is available at [this link](https://myceliumnft.netlify.app/)

## Contributing

We welcome contributions from the community. If you wish to contribute, please take a moment to review our [Contributing Guidelines](CONTRIBUTING.md).

## Support

If you encounter any issues while using the Mycelium API Server or have any feature requests, please file an issue on the [GitHub issues page](https://github.com/lst68868/mycelium-api/issues).

## License

The Mycelium API Server is licensed under the [MIT License](LICENSE).

## Acknowledgements

We would like to thank the open-source community for their continuous support and inspiration. We're excited to be a part of the journey to make NFT minting accessible to everyone.

## Contact

For any queries, feel free to reach out to us at [lst68868@gmail.com](mailto:lst68868@gmail.com).
