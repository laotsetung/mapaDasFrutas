if (icone == undefined){
    var icone=0
}else if (icone == ""){
    var icone=0
}

if(document.getElementById('lat')== undefined || document.getElementById('lat').value == "" ){
    var lat = localStorage.getItem("lat");//document.getElementById('lat').value
}
if (document.getElementById('lon') == undefined || document.getElementById('lon').value == ""){
    var lon = localStorage.getItem("lon");//document.getElementById('lon').value
}

document.write(`
  <div id="cabecalho" class="cabecalho">    
    <table class="tabCab" style="">
        <tr>`);

    document.write(`<td style="width: 25%;"></td>`);

document.write(`<td style="width: 25%; text-align: center;">
            <div class="dropdown">
            <button class="dropbtn btn-menu"><img src="../static/imgs/btnPrincipal_v2.png" alt="" title="Menu"></button>
            <div class="dropdown-content">
                <a href="/">Atualizar Mapa</a>`);

                document.write(`<a href="/estacao/${lat};${lon}">Frutas da Estação</a>`)
                
                // document.write(`<a href="#">Mapa por Fruta</a>`)

                /*if(usuario == undefined){
                    document.write(`<span style='text-decoration: line-through; font-size: 24px' title='Fazer Login Para Adicionar'> Nova Fruta</span>`);
                }else{
                    document.write(`<a href="/local">Nova Fruta</a>`);
                }*/
                if(usuario != ""){
                    document.write(`<a href="/local">Nova Fruta</a>`);
                }else{
                    document.write(`<span style='text-decoration: line-through; font-size: 24px' title='Fazer Login Para Adicionar'>Nova Fruta</span>`);
                }
                
                document.write(`
                <a href="/verUsuarios">Lista de Usuarios</a>
                <a href="/estatisticas">Estatisticas</a>
                <a href="/sobre">Sobre</a>
                
            </div>
            </div>
        </td>

        <td style="width: 25%; text-align: center;">
            <div class="dropdown">
                <button class="dropbtn btn-perfil">
                <img src="../static/imgs/icone_perfil/perfil0${icone}.png" alt="" title="Perfil" class="imgPerfil">
                </button>
                <div class="dropdown-content-2">`)

                if (usuario != ""){
                    document.write(`<span style='font-size: 20px; color: white'> ${usuario} </span>
                    <a href="/perfil/${userId}">Perfil</a>
                    <a href="/logout">Logout</a>`)
                }else{

                    
                    document.write(`
                        <div style='margin-top: 15px'>
                        <form action="/login" method="post" enctype="multipart/form-data">
                        <table>
                        <tr><td colspan=2 style='font-size: 20px'>Login:</td></tr>
                        <tr>
                            <td><label for="usuario">Usuario:</label></td>
                            <td><input type="text" name="usuario" id="usuario" style="width: 135px"></td>
                        </tr>
                        <tr><td colspan=2 style='padding: 5px' /></tr>

                        <tr>
                            <td><label for="senha">Senha:</label></td>
                            <td><input type="password" name="senha" id="senha" style="width: 135px"></td>
                        </tr>
                        <tr>
                            <td colspan="2">
                                <button class="btnEnviar">Logar</button>
                            </td>
                        </tr>
                    </table>
                    </form>
                        
                        </div>
                    `)

                    
                    document.write(`<div style='margin-top: 15px; background-color: var(--fundo);'>
                    Não tem uma conta?
                    <a href="/cadastrar">Cadastrar</a>
                    </div>`);
                }
                document.write(`</div>
            </div>
        </td>

        <td style="width: 25%; font-size: 12px"> v_1.0</td>
        </tr>
    </table>
  </div>`);