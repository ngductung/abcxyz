// Beautiful
javascript: (function() {
    idProject = location.href.split('/')[5];
    var url = 'https://pentest.viettelcyber.com/api/task/' + idProject + '/checklist/210';
    var headers = new Headers();
    headers.append('Token', localStorage.getItem('token'));
    var request = new Request(url, {
        method: 'GET',
        headers: headers
    });
    var responseData;
    fetch(request).then(function(response) {
        if (response.ok) {
            return response.json();
        } else {
            alert('ERROR');
        }
    }).then(function(data) {
        responseData = data;
        var ids = [];
        for (var i = 0; i < responseData.length; i++) {
            var checklist = responseData[i].checkList;
            for (var j = 0; j < checklist.length; j++) {
                var id = checklist[j].id;
                ids.push(id);
                continue;
            }
        }
        totalRequests = ids.length;
        for (var i = 0; i < ids.length; i++) {
            var putData = {
                taskAssigneeBugListId: ids[i],
                status: 'CHECKED'
            };
            var headers = new Headers();
            headers.append('Content-Type', 'application/json');
            newURL = 'https://pentest.viettelcyber.com/api/task/checklist/change';
            headers.append('Token', localStorage.getItem('token'));
            var requestPUT = new Request(newURL, {
                method: 'PUT',
                headers: headers,
                body: JSON.stringify(putData)
            });
            var successfulRequests = 0;
            fetch(requestPUT).then(function(response) {
                if (response.ok) {
                    successfulRequests++;
                    if (successfulRequests === totalRequests) {
                        alert('DONE');
                        window.location.reload();
                    }
                }
            });
        }
    });
})()

// One line for bookmark
javascript:(function() {idProject = location.href.split('/')[5];var url = 'https://pentest.viettelcyber.com/api/task/' + idProject + '/checklist/210';var headers = new Headers();headers.append('Token', localStorage.getItem('token'));var request = new Request(url, {method: 'GET',headers: headers});var responseData;fetch(request).then(function(response) {if (response.ok) {return response.json();} else {alert('ERROR');}}).then(function(data) {responseData = data;var ids = [];for (var i = 0; i < responseData.length; i++) {var checklist = responseData[i].checkList;for (var j = 0; j < checklist.length; j++) {var id = checklist[j].id;ids.push(id);continue;}}totalRequests = ids.length;for (var i = 0; i < ids.length; i++) {var putData = {taskAssigneeBugListId: ids[i],status: 'CHECKED'};var headers = new Headers();headers.append('Content-Type', 'application/json');newURL = 'https://pentest.viettelcyber.com/api/task/checklist/change';headers.append('Token', localStorage.getItem('token'));var requestPUT = new Request(newURL, {method: 'PUT',headers: headers,body: JSON.stringify(putData)});var successfulRequests=0;fetch(requestPUT).then(function(response) {if (response.ok) {successfulRequests++;if (successfulRequests === totalRequests) {alert('DONE');window.location.reload();}}});}});})()
