//Create function to take in a selected stat and plot it on a bar graph for each name, role.
function buildBarGraph(stat) {
    //Import JSON file.
    d3.json('json/game_data.json').then((data) => {
        //Create empty arrays to store data.
        let name_position_list = [];
        let stat_list = [];

        //Iterate over data to push name, role to first list and selected stat to second list.
        for (let i = 0; i < data.length; i++) {
            name_position_list.push(`${data[i]['summonerName']}, ${data[i]['individualPosition']}`);
            let numb = data[i][stat].toFixed(2);
            stat_list.push(numb);
        };

        //Build bar graph.
        let barData = [{
                x: name_position_list,
                y: stat_list,
                type: 'bar',
                opacity: 0.5,
                text: stat_list.map(String),
                textposition: 'inside',
                textangle: 0,
                hoverinfo: 'none',
                marker: {
                    color: 'rgb(179, 0, 0)'
                }
            }];

        //Plot bar graph.    
        Plotly.newPlot('bar', barData, {xaxis: {tickangle: 45}});

    });
};

//Create function to display dropdown menu and initial data.
function init() {
    //Create dropdown menu.
    let selector = d3.select('#selDataset');

    //Import JSON file.
    d3.json('json/game_data.json').then((data) => {

        //Create list of stats and iterate over to add into dropdown menu.
        all_stat_list = Object.keys(data[0]);

        for (let i = 2; i < all_stat_list.length; i++) {
            selector.append('option')
                    .text(all_stat_list[i])
                    .property('value', all_stat_list[i]);
        };

        //Use number of games as initial displayed data.
        buildBarGraph(all_stat_list[2]);

    });
};

//Create a function to change bar graph based on dropdown selection.
function optionChanged(new_stat) {
    buildBarGraph(new_stat);
};

//Initialize.
init();

//Create function to take in a selected pick ban stat and plot it on a bar graph for each champion name.
function buildBarGraph2(stat) {
    //Import JSON file.
    d3.json('json/pick_ban.json').then((data) => {
        //Create empty arrays to store data.
        let champion_name_list = [];
        let stat_list = [];
        
        //Iterate over data to push champion name to first list and selected pick ban stat to second list.
        for (let i = 0; i < data.length; i++) {
            champion_name_list.push(data[i]['championName']);
            let numb = data[i][stat].toFixed(2);
            stat_list.push(numb);
        };

        //Build bar graph.
        let barData = [{
                x: champion_name_list,
                y: stat_list,
                type: 'bar',
                opacity: 0.5,
                text: stat_list.map(String),
                textposition: 'inside',
                textangle: 90,
                hoverinfo: 'none',
                marker: {
                    color: 'rgb(0, 102, 0)'
                }
            }];

        //Plot bar graph.
        Plotly.newPlot('bar2', barData, {xaxis: {tickangle: 45}});

    });
};

//Create function to display dropdown menu and initial data.
function init2() {
    //Create dropdown menu.
    let selector = d3.select('#selDataset2');

    //Import JSON file.
    d3.json('json/pick_ban.json').then((data) => {

        //Create list of stats and iterate over to add into dropdown menu.
        all_stat_list = Object.keys(data[0]);

        for (let i = 1; i < all_stat_list.length; i++) {
            selector.append('option')
                    .text(all_stat_list[i])
                    .property('value', all_stat_list[i]);
        };

        //Use pick ban percent as initial displayed data.
        buildBarGraph2(all_stat_list[1]);

    });
};

//Create a function to change bar graph based on dropdown selection.
function optionChanged2(new_stat) {
    buildBarGraph2(new_stat);
};

//Initialize.
init2();

//Create function to display head to head record in a table.
function buildOppTeamTable() {
    //Import JSON file.
    d3.json('json/head_to_head.json').then((data) => {
        
        //Create list of players to serve as columns and rows.
        players_list = ['', 'Andy', 'Anthony', 'Beals', 'Desp', 'Furb', 'Jackson', 'Jess', 'Kinga',
                        'Kori', 'Luke', 'Milroy', 'Moo', 'Nick B.', 'Nick D.', 'Rob', 'Tonnie', 'Tyler'];

        players_list2 = ['Andy', 'Anthony', 'Beals', 'Desp', 'Furb', 'Jackson', 'Jess', 'Kinga',
                        'Kori', 'Luke', 'Milroy', 'Moo', 'Nick B.', 'Nick D.', 'Rob', 'Tonnie', 'Tyler'];
        
        //Create empty array to store data.
        table_list = [];
        
        //Iterate over data and push record to empty array.
        for (let i = 0; i < data.length; i++) {
            for (let j = 0; j < data.length; j++) {
                table_list.push(data[j][i])
            };
        };

        //Slice array into multiple arrays such that each array is a column in the table. 
        z = players_list2.length;
        table_list_0 = table_list.slice(0, z);
        table_list_1 = table_list.slice(z, 2*z);
        table_list_2 = table_list.slice(2*z, 3*z);
        table_list_3 = table_list.slice(3*z, 4*z);
        table_list_4 = table_list.slice(4*z, 5*z);
        table_list_5 = table_list.slice(5*z, 6*z);
        table_list_6 = table_list.slice(6*z, 7*z);
        table_list_7 = table_list.slice(7*z, 8*z);
        table_list_8 = table_list.slice(8*z, 9*z);
        table_list_9 = table_list.slice(9*z, 10*z);
        table_list_10 = table_list.slice(10*z, 11*z);
        table_list_11 = table_list.slice(11*z, 12*z);
        table_list_12 = table_list.slice(12*z, 13*z);
        table_list_13 = table_list.slice(13*z, 14*z);
        table_list_14 = table_list.slice(14*z, 15*z);
        table_list_15 = table_list.slice(15*z, 16*z);
        table_list_16 = table_list.slice(16*z, 17*z);

        //Build table.
        tableData = [{
            type: 'table',
            header: {
                values: players_list
            },
            cells: {
                values: [players_list2, table_list_0, table_list_1, table_list_2, table_list_3, table_list_4, table_list_5, table_list_6, table_list_7, table_list_8, table_list_9,
                         table_list_10, table_list_11, table_list_12, table_list_13, table_list_14, table_list_15, table_list_16]
            }
        }];

        //PLot table.
        Plotly.newPlot('table', tableData, {height: 550});

    });
};

//Initialize.
buildOppTeamTable();

//Create function to display record of players on the same team in a table.
function buildSameTeamTable() {
    //Import JSON file.
    d3.json('json/same_team.json').then((data) => {
        
        //Create list of players to serve as columns and rows.
        players_list = ['', 'Andy', 'Anthony', 'Beals', 'Desp', 'Furb', 'Jackson', 'Jess', 'Kinga', 'Kori', 'Luke', 'Milroy', 'Moo', 'Nick B.', 'Nick D.', 'Rob', 'Tonnie', 'Tyler'];

        players_list2 = ['Andy', 'Anthony', 'Beals', 'Desp', 'Furb', 'Jackson', 'Jess', 'Kinga', 'Kori', 'Luke', 'Milroy', 'Moo', 'Nick B.', 'Nick D.', 'Rob', 'Tonnie', 'Tyler'];
        
        //Create empty array to store data.
        table_list = [];

        //Iterate over data and push record to empty array.
        for (let i = 0; i < data.length; i++) {
            for (let j = 0; j < data.length; j++) {
                table_list.push(data[j][i])
            };
        };

        //Slice array into multiple arrays such that each array is a column in the table.
        z = players_list2.length;
        table_list_0 = table_list.slice(0, z);
        table_list_1 = table_list.slice(z, 2*z);
        table_list_2 = table_list.slice(2*z, 3*z);
        table_list_3 = table_list.slice(3*z, 4*z);
        table_list_4 = table_list.slice(4*z, 5*z);
        table_list_5 = table_list.slice(5*z, 6*z);
        table_list_6 = table_list.slice(6*z, 7*z);
        table_list_7 = table_list.slice(7*z, 8*z);
        table_list_8 = table_list.slice(8*z, 9*z);
        table_list_9 = table_list.slice(9*z, 10*z);
        table_list_10 = table_list.slice(10*z, 11*z);
        table_list_11 = table_list.slice(11*z, 12*z);
        table_list_12 = table_list.slice(12*z, 13*z);
        table_list_13 = table_list.slice(13*z, 14*z);
        table_list_14 = table_list.slice(14*z, 15*z);
        table_list_15 = table_list.slice(15*z, 16*z);
        table_list_16 = table_list.slice(16*z, 17*z);

        //Build table.
        tableData = [{
            type: 'table',
            header: {
                values: players_list
            },
            cells: {
                values: [players_list2, table_list_0, table_list_1, table_list_2, table_list_3, table_list_4, table_list_5, table_list_6, table_list_7, table_list_8, table_list_9,
                         table_list_10, table_list_11, table_list_12, table_list_13, table_list_14, table_list_15, table_list_16]
            }
        }];

        //Plot table.
        Plotly.newPlot('table2', tableData, {height: 550});

    });
};

//Initialize.
buildSameTeamTable();

//Create function to display win percent.
function buildWinrateTable() {
    //Import JSON file.
    d3.json('json/winrate.json').then((data) => {

         //Create list of players to serve as rows.
        players_list = ['Andy', 'Anthony', 'Beals', 'Desp', 'Furb', 'Jackson', 'Jess', 'Kinga', 'Kori', 'Luke', 'Milroy', 'Moo', 'Nick B.', 'Nick D.', 'Rob', 'Tonnie', 'Tyler'];

        //Create list of stats to serve as column headers.
        headers_list = ['', 'NumberOfGames', 'Wins', 'Losses', 'WinPercent'];

        //Create empty array to store data.
        table_list = [];
        
        //Iterate over data and push record to empty array.
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < data.length; j++) {
                table_list.push(data[j][i])
            };
        };
        
        //Create empty array to store data.
        table_list_3 = [];

        //Iterate over data and push record to empty array.
        for (let i = 0; i < data.length; i++) {
            table_list_3.push(data[i][3].toFixed(2))
        };

        //Slice array into multiple arrays such that each array is a column in the table.
        z = players_list.length;
        table_list_0 = table_list.slice(0, z);
        table_list_1 = table_list.slice(z, 2*z);
        table_list_2 = table_list.slice(2*z, 3*z);
        
        tableData = [{
            type: 'table',
            header: {
                values: headers_list
            },
            cells: {
                values: [players_list, table_list_0, table_list_1, table_list_2, table_list_3]
            }
        }];

        //Plot table.
        Plotly.newPlot('table3', tableData, {height: 550});
        
    });
};

//Initialize.
buildWinrateTable();