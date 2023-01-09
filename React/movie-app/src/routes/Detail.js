import { useEffect ,useState} from "react";
import {useParams} from "react-router-dom";

function Detail(){
    const {id} = useParams(); // route로 넘겨받은 변수가 담김
    const [movie, setMovie] = useState([]);
    const getMovie = async() => {
        const json = await (
            await fetch(
                `https://yts.mx/api/v2/movie_details.json?movie_id=${id}`
            )
        ).json();
        setMovie(json.data.movie);
    }
    useEffect(() => {
        getMovie();
    },[]);
    console.log(movie);

    return(
        <div>
            <h1>{movie.title}</h1>
            <h3>{movie.year}</h3>
            <div>{movie.genres.map(m =>
                <ul>
                    <li>{m}</li>
                </ul>
            )}</div>
        </div>);
};
export default Detail;