
import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect } from "react";
import Link from 'next/link'
import styled from "styled-components";
const S_SigninForm = styled.form`
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
  height:100%;
`;
const DIV = styled.div`
position: fixed;
width: 100%;
top: 200px;`;


const S_Form = styled.input`
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
  &:focus {
    z-index: 2;
  }
`;

const S_EmailForm = styled(S_Form)`
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
`;

const S_PasswordForm = styled(S_Form)`
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
`;



function Home() {


    const router = useRouter();
    useEffect(() => {

        localStorage.removeItem("username");
    }, []);
    function a(username) {
        const b = '1'
        localStorage.setItem("username", username);
        router.push({
            pathname: `/list/${b}`,
            query: { username: username },
          });
        
    }
    async function onSubmit(event) {

        let login = false;
        event.preventDefault();
        console.log(event.target.childNodes[1].value);
        console.log(event.target.childNodes[2].value);
        const username = event.target.childNodes[1].value;
        const password = event.target.childNodes[2].value;
        event.target.childNodes[1].value = "";
        event.target.childNodes[2].value = "";
        const res = await (await fetch(`/api/users/${username}`)).json();
        res.result === null ? login = false : login = true;
        if (login) {
            password === res.result.password ? a(res.result.username) : alert("Wrong Password!");
        }
        else { alert("No Such Username!"); }


    }
    return (

        <DIV>

            <Head>
                <title>Home</title>
            </Head>

            <S_SigninForm onSubmit={onSubmit} className="form-signin text-center" >

                <h1 className="h3 mb-3 fw-normal">Please sign in</h1>

                <S_EmailForm
                    type="text"
                    id="inputEmail"
                    className="form-control"
                    placeholder="Username"
                    required={true}
                    autoFocus={true}
                />

                <S_PasswordForm
                    type="password"
                    id="inputPassword"
                    className="form-control"
                    placeholder="Password"
                    required={true}
                />

                <button className="w-100 btn btn-lg btn-dark" >
                    Sign in
                </button>
                <Link href="/signup">
                    <a>Sign up</a>
                </Link>
                <p className="mt-5 mb-3 text-muted">&copy; 2017-2020</p>
            </S_SigninForm>


        </DIV>
    );
}

export default Home;

