name: BalanceService
version: ""
description: Services to interact with the blockchain database
lifecycle: null
__proto:
    package: balanceservice
    targetfile: balance.proto
    imports:
        - google/api/annotations.proto
        - balanceservice/reqmsgs.proto
        - google/protobuf/empty.proto
        - balance/balance.proto
    options:
        go_package: github.com/maltenorstroem/tbb-api-spec/balanceservice;balanceservicepb
        java_multiple_files: "true"
        java_outer_classname: BalanceProto
        java_package: com.github.maltenorstroem.tbb.api.balanceservice
services:
    List:
        description: List of all wallets
        data:
            request: google.protobuf.Empty
            response: balance.BalanceCollection
            bodyfield: body
        deeplink:
            description: 'List: GET /balances google.protobuf.Empty , balance.BalanceCollection #List of all wallets'
            href: /balances
            method: GET
            rel: list
        query: {}
        rpc_name: ListBalances
